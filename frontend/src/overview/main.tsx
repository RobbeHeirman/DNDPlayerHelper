import React from 'react'
import ReactDOM from 'react-dom/client'
import axios from "axios";

axios.defaults.baseURL = `${import.meta.env.VITE_BASE_URL ||"127.0.0.1:8000"}`

function createNewSheet() {
    axios.post(`character_sheet/create_sheet`, {}, )
        .then(() => alert("Created"))
        .catch((e) => alert(e))
}

ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <button onClick={createNewSheet}>Create new sheet</button>
    </React.StrictMode>,
)
