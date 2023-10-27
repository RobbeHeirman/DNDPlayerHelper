export type InputFieldProps = {
    type: string
    fieldName: string
    onChange: (value: any) => void
}

function InputField(props: InputFieldProps) {
    return (
        <>
            <label htmlFor={props.fieldName}>{props.fieldName}</label><input type={props.type} name={props.fieldName}/>
        </>
    )
}

export default InputField;