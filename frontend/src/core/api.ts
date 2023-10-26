import axios, {AxiosPromise} from "axios";

axios.defaults.baseURL = `${import.meta.env.VITE_BASE_URL ||"127.0.0.1:8000"}`

export function post<Type>(route: string, data: Object | null = null): AxiosPromise<Type> {
    return axios.post<Type>(route, data)
}