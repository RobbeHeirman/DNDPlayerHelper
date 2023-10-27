import InputField from "./input_field.tsx";

type TextInputFieldProps =  {
    fieldName: string,
    onChange: (value:string) => void
}

export default function TextInputField(props: TextInputFieldProps) {
    return <InputField {...props} type={"text"}/>
}