type InputFieldProps = {
    fieldName: string
    onChange: (value: any) => void
}

function InputField(props: InputFieldProps) {
    return (
        <>
            <label htmlFor={props.fieldName}>{props.fieldName}</label><input name={props.fieldName}/>
        </>
    )
}

export default InputField;