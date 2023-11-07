import {useCallback, useEffect, useState} from 'react';
import useWebSocket from 'react-use-websocket';
import {CharacterSheet, CharacterSheetService, OpenAPI} from "../../client";
import InputField from "./components/input_field.tsx";
import './style.css'
import ObserverManager from "../../core/ObserverManager.ts";

function _getSheetId() {
    const urlParams = new URLSearchParams(window.location.search);
    return parseInt(urlParams.get("id") || "0"); // TODO: Fix some handling if bad call
}

export type SocketMessage = {
    // Socket will always send data about one of the character fields
    field: keyof CharacterSheet,
    data: string
}

export type MessageHandler = (message: SocketMessage) => void
const broadCast: ObserverManager<SocketMessage> = new ObserverManager();
export const Sheet = () => {

    const [initSheet, setInitSheet] = useState<CharacterSheet | null>(null)

    // Set up a websocket connection
    const sheet_id = _getSheetId();
    const socketUrl = `${OpenAPI.BASE.replace("http", "ws")}/character_sheet/socket/${sheet_id}`
    const {sendMessage, lastMessage} = useWebSocket(socketUrl);

    useEffect(() => {
        // TODO: Handle failed fetch
        CharacterSheetService.getSheet(sheet_id).then(sheet => setInitSheet(sheet));
    }, []);

    useEffect(() => {
        if (lastMessage !== null) {
            broadCast.broadcast(JSON.parse(lastMessage.data))
        }
    }, [lastMessage]);

    const doSendMessage = useCallback(
        (message: SocketMessage) => sendMessage(JSON.stringify(message)),
        []
    );

    const fieldFactory = useCallback((type: string, displayName: string, fieldName: keyof CharacterSheet) =>
         InputField<string | number>({
            displayName: displayName,
            type: type,
            initialValue: initSheet?.[fieldName]?? "",
            fieldName: fieldName,
            observer: broadCast,
            onChange: doSendMessage
        })
    , [initSheet])

    return (
        <div>
            <div className="charsheet" id="root">
                <header>
                    <section className="charname">
                        {fieldFactory("text", "Character Name", "character_name")}
                    </section>
                    <section className="misc">
                        <ul>
                            <li>
                                // TODO: Race in the backend.
                                {fieldFactory('text', 'Race', 'race')}
                            </li>
                        </ul>
                    </section>
                </header>
            </div>
        </div>
    );
};

// function Sheet() {
//
//     const [characterSheet, setCharacterSheet] = useState<CharacterSheet>();
//
//     useEffect(() => {
//         const urlParams = new URLSearchParams(window.location.search);
//         const id = urlParams.get('id') || "0";
//         const myParam = Number.parseInt(id);
//         CharacterSheetService.getSheet(myParam).then(sheet => setCharacterSheet(sheet));
//     }, []);
//
//
//     return (
//         <div>
//             <form className="charsheet" id="root">
//                 <header>
//                     <section className="charname">
//                         <label htmlFor="charname">Character Name</label>
//                         <input name="charname"/>
//                     </section>
//                     <section className="misc">
//                         <ul>
//                             {/*<li>*/}

//                             {/*</li>*/}
//                             <li>
//                                 <label htmlFor="background">Background</label><input name="background"
//                                                                                      placeholder="Acolyte"/>
//                             </li>
//                             <li>
//                                 <label htmlFor="level">Level</label><input name="Level"
//                                                                                       placeholder="1"/>
//                             </li>
//                             <li>
//                                 <label htmlFor="race">Race</label><input name="race" placeholder="Half-elf"/>
//                             </li>
//                             <li>
//                                 <label htmlFor="alignment">Alignment</label><input name="alignment"
//                                                                                    placeholder="Lawful Good"/>
//                             </li>
//                             <li>
//                                 <label htmlFor="experiencepoints">Experience Points</label><input
//                                 name="experiencepoints"
//                                 placeholder="3240"/>
//                             </li>
//                         </ul>
//                     </section>
//                 </header>
//             </form>
//         </div>
//     )
// }


export default Sheet
