import './style.css'
import React, {useEffect, useState} from "react";
import TextInputField from "./components/text_input_field.tsx";
import ReactDOM from "react-dom/client";
import {CharacterSheet, CharacterSheetService} from "../../client";

function Sheet() {

    const [characterSheet, setCharacterSheet] = useState<CharacterSheet>();

    useEffect(() => {
        const urlParams = new URLSearchParams(window.location.search);
        const id = urlParams.get('id') || "0";
        const myParam = Number.parseInt(id);
        CharacterSheetService.getSheet(myParam).then(sheet => setCharacterSheet(sheet));
    }, []);


    return (
        <div>
            <form className="charsheet" id="root">
                <header>
                    <section className="charname">
                        <label htmlFor="charname">Character Name</label>
                        <input name="charname"/>
                    </section>
                    <section className="misc">
                        <ul>
                            {/*<li>*/}
                            {/*    <TextInputField fieldName="Class"*/}
                            {/*                    onChange={(value) => setCharacterSheet(Object.assign(characterSheet, {class: value}))}/>*/}
                            {/*</li>*/}
                            <li>
                                <label htmlFor="background">Background</label><input name="background"
                                                                                     placeholder="Acolyte"/>
                            </li>
                            <li>
                                <label htmlFor="level">Level</label><input name="Level"
                                                                                      placeholder="1"/>
                            </li>
                            <li>
                                <label htmlFor="race">Race</label><input name="race" placeholder="Half-elf"/>
                            </li>
                            <li>
                                <label htmlFor="alignment">Alignment</label><input name="alignment"
                                                                                   placeholder="Lawful Good"/>
                            </li>
                            <li>
                                <label htmlFor="experiencepoints">Experience Points</label><input
                                name="experiencepoints"
                                placeholder="3240"/>
                            </li>
                        </ul>
                    </section>
                </header>
            </form>
        </div>
    )
}

ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <Sheet/>
    </React.StrictMode>,
)

