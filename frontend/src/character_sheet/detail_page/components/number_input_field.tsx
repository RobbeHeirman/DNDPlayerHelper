import InputField from "./input_field.tsx";

type TextInputFieldProps =  {
    fieldName: string,
    onChange: (value:number) => void
}

export default function NumberInputField(props: TextInputFieldProps) {
    return <InputField {...props} type={"number"}/>
}