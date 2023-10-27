import React, {useEffect, useState} from 'react'
import ReactDOM from 'react-dom/client'
import CharacterSheetModel, {
    createRemoteSheet,
    getRemoteSheetList
} from "../models/character_sheet_model.ts";


function Overview() {

    const [sheets, setSheet] = useState(new Array<CharacterSheetModel>());

    function createNewSheet() {

        createRemoteSheet().then(result => setSheet([...sheets, result]));
    }


    useEffect(() => {
        getRemoteSheetList().then(value => setSheet(value))
    }, []);
    return (
        <>
            <button onClick={createNewSheet}>Create new sheet</button>
            <ul>
                {sheets.map((value) => <li><a>{value.id} {value.character_name}</a></li>)}
            </ul>
            </>
    )
}


ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <Overview></Overview>
    </React.StrictMode>,
)
