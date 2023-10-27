import React, {useEffect, useState} from 'react'
import ReactDOM from 'react-dom/client'
import {CharacterSheetService} from "../../client";
import {CharacterSheet} from "../../client";


function Overview() {

    const [sheets, setSheet] = useState(new Array<CharacterSheet>());

    function createNewSheet() {
        CharacterSheetService.createSheet().then(result => setSheet([...sheets, result]));
    }


    useEffect(() => {
        CharacterSheetService.getSheets().then(value => setSheet(value))
    }, []);
    return (
        <>
            <button onClick={createNewSheet}>Create new sheet</button>
            <ul>
                {sheets.map((value) =>
                    <li key={value.id}>
                        <a href={`/character_sheet/html/detail.html?id=${value.id}`}>{value.id} {value.character_name}</a>
                    </li>
                )}
            </ul>
        </>
    )
}


ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <Overview></Overview>
    </React.StrictMode>,
)
