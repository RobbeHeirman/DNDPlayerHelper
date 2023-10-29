import React, {useCallback} from "react";

export type InputFieldProps = {
    type: string
    fieldName: string
    onChange: (value: any) => void
}

function InputField(props: InputFieldProps) {
    const fieldChange = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
        e.preventDefault();
        props.onChange(e.target.value);
    }, []);

    return (
        <>
            <label htmlFor={props.fieldName}>{props.fieldName}</label>
            <input onChange={fieldChange} type={props.type} name={props.fieldName}/>
        </>
    )
}

export default InputField;