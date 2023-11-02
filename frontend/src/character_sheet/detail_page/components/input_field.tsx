import React, {useCallback} from "react";

export type InputFieldProps = {
    type: string
    fieldName: string
    onChange: (value: any) => void
    value: string
}

function InputField(props: InputFieldProps) {
    const fieldChange = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
        //e.preventDefault();
        props.onChange(e.target.value);
    }, []);

    return (
        <>
            <label htmlFor={props.fieldName}>{props.fieldName}</label>
            <input onChange={fieldChange} type={props.type} name={props.fieldName} value={props.value}/>
        </>
    )
}

export default InputField;