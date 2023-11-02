import InputField from "./input_field.tsx";
import {useEffect, useState} from "react";
import {MessageHandler, SocketMessage} from "../sheet.tsx";

type TextInputFieldProps =  {
    fieldName: string,
    initialValue: string
    onChange: (value:string) => void,
    subscribersSet: (handle: MessageHandler) => void
    postCall: (message: SocketMessage) => void
}

export default function TextInputField(props: TextInputFieldProps) {
    const [value, setValue] = useState<string>(props.initialValue);

    useEffect(() => {
            const sub = (message: SocketMessage) => {
                if(message.field === props.fieldName){
                    setValue(message.data);
                }
            }
            props.subscribersSet(sub);

    }, []);

    function onChange(e: string) {
        //e.preventDefault();
        const val = e
        setValue(val);
        const message: SocketMessage =  {
            field: props.fieldName,
            data: val
        }
        props.postCall(message);
    }

    return <InputField {...props} type={"text"} value={value} onChange={e =>onChange(e)}/>
}