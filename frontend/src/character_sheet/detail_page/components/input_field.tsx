import {SocketMessage} from "../sheet.tsx";
import React, {useEffect, useState} from "react";
import {CharacterSheet} from "../../../client";
import ObserverManager from "../../../core/ObserverManager.ts";

export type InputFieldProps<T> = {
    type: string
    displayName: string
    initialValue: T
    fieldName: keyof CharacterSheet
    observer: ObserverManager<SocketMessage>
    onChange: (message: SocketMessage) => void

}

export default function InputField<T>(props: InputFieldProps<T>) {
    const {
        type,
        displayName,
        initialValue,
        fieldName,
        observer,
        onChange,
        ...inProps
    } = props
    const [value, setValue] = useState<T>(props.initialValue);
    useEffect(() => {
        const sub = (message: SocketMessage) => {
            if (message.field !== fieldName) return
            setValue(message.data as T);
        }
        observer.subscribe(sub);
        return () => observer.unsubscribe(sub);
    }, []);

    useEffect(() => {
        setValue(initialValue)
    }, [initialValue]);

    function inOnChange(e: React.ChangeEvent<HTMLInputElement>) {
        //e.preventDefault();
        const val = e.target.value as T
        setValue(val);
        const message: SocketMessage = {
            field: fieldName,
            data: String(val)
        }
        onChange(message);
    }

    return <>
        <label htmlFor={fieldName}>{displayName}</label>
        <input type={type}
               id={fieldName}
               value={String(value)}
               onChange={inOnChange}
               {...inProps}
        />
    </>
}
