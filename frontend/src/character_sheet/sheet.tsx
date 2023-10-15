import '../style.css'
import {useState} from "react";
import CharacterSheetModel from "./models/character_sheet_model.ts";
import TextInputField from "./components/text_input_field.tsx";

function Sheet() {

    const [characterSheet, setCharacterSheet]  = useState(new CharacterSheetModel(0))
    return (
        <form className="charsheet" id="root">
            <header>
                <section className="charname">
                    <label htmlFor="charname">Character Name</label>
                    <input name="charname"/>
                </section>
                <section className="misc">
                    <ul>
                        <li>
                            <TextInputField fieldName="Class" onChange={(value) => setCharacterSheet(Object.assign(characterSheet, {class: value}))}/>
                        </li>
                        <li>
                            <label htmlFor="background">Background</label><input name="background" placeholder="Acolyte"/>
                        </li>
                        <li>
                            <label htmlFor="playername">Player Name</label><input name="playername" placeholder="Player McPlayerface"/>
                        </li>
                        <li>
                            <label htmlFor="race">Race</label><input name="race" placeholder="Half-elf"/>
                        </li>
                        <li>
                            <label htmlFor="alignment">Alignment</label><input name="alignment" placeholder="Lawful Good"/>
                        </li>
                        <li>
                            <label htmlFor="experiencepoints">Experience Points</label><input name="experiencepoints"
                                                                                              placeholder="3240"/>
                        </li>
                    </ul>
                </section>
            </header>
        </form>
    )
}

export default Sheet
