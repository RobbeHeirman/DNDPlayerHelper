

export type InputFieldProps = {
    type: string
    fieldName: string
    value: string
    onChange: (event: any) => void
}

function InputField(props: InputFieldProps) {
    // const fieldChange = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    //     e.preventDefault();
    //     props.onChange(e.target.value);
    // }, []);
    //


    return (
        <>
            <label htmlFor={props.fieldName}>{props.fieldName}</label>
            <input key={props.value} onChange={props.onChange} type={props.type} name={props.fieldName} value={props.value}/>
        </>
    )
}

export default InputField;