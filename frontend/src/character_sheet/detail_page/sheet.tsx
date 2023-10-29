import {useCallback, useEffect} from 'react';
import useWebSocket from 'react-use-websocket';
import TextInputField from "./components/text_input_field.tsx";

const urlParams = new URLSearchParams(window.location.search);
const sheet_id = parseInt(urlParams.get("id") || "0"); // TODO: Fix some handling if bad call

export const Sheet = () => {
    const {sendMessage, lastMessage} = useWebSocket('ws://localhost:8000/character_sheet/socket');
    useEffect(() => {
        if (lastMessage !== null) {
        }
    }, [lastMessage]);

    const updateDataFunctionFactory = useCallback(<T, >(field: String) => {
        return (data: T) => {
            sendMessage(JSON.stringify({
                id: sheet_id,
                field: field,
                data: data
            }))
        }
    }, [])

    return (
        <div>
            <div className="charsheet" id="root">
                <header>
                    <TextInputField fieldName={"Character Name"} onChange={updateDataFunctionFactory("character_name")}/>
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
