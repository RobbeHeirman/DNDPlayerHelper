import React from 'react'
import ReactDOM from 'react-dom/client'
import {createRemoteSheet} from "../character_sheet/models/character_sheet_model.ts";

function createNewSheet() {
    createRemoteSheet().then(result => console.log(result.id));
}

function Overview() {


    return (

        <button onClick={createNewSheet}>Create new sheet</button>
    )

}

ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <Overview></Overview>
    </React.StrictMode>,
)
