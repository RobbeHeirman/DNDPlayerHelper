import {useCallback, useEffect, useState} from 'react';
import useWebSocket from 'react-use-websocket';
import TextInputField from "./components/text_input_field.tsx";
import {CharacterSheetService, CharacterSheet} from "../../client";


export type SocketMessage = {
    field: string,
    data: string
}

export type MessageHandler = (message: SocketMessage) =>void
export const Sheet = () => {
    let characterSheet!: CharacterSheet;

    const urlParams = new URLSearchParams(window.location.search);
    const sheet_id = parseInt(urlParams.get("id") || "0"); // TODO: Fix some handling if bad call
    const socketUrl = `ws://localhost:8000/character_sheet/socket/${sheet_id}`
    const {sendMessage, lastMessage} = useWebSocket(socketUrl);

    const [subscribers, setSubscribers] = useState<MessageHandler[]>([])
    function setSubscriber(message: MessageHandler ) {
        setSubscribers([...subscribers, message]);
    }
    useEffect(() => {
        CharacterSheetService.getSheet(sheet_id).then(sheet => characterSheet = sheet);
    }, []);

    useEffect(() => {
        if (lastMessage !== null) {
            console.log(subscribers)
            subscribers.forEach(subscriber => subscriber(JSON.parse(lastMessage.data)));
        }
    }, [lastMessage]);

    const updateDataFunctionFactory = useCallback(<T, >(field: String) => {
        return (data: T) => {
            sendMessage(JSON.stringify({
                field: field,
                data: data
            }))
        }
    }, [])

    function doSendMessage(message: SocketMessage){
        sendMessage(JSON.stringify(message));
    }

    return (
        <div>
            <div className="charsheet" id="root">
                <header>
                    <TextInputField fieldName={"character_name"}
                                    onChange={updateDataFunctionFactory("character_name")}
                                    initialValue={characterSheet?.character_name || ''}
                                    postCall={doSendMessage}
                                    subscribersSet={setSubscriber}
                    />
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
