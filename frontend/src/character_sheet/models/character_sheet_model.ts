import {get, post} from "../../core/api.ts";

export default class CharacterSheetModel {
    id: number
    character_name: string
    class: string
    level: number

    constructor(args: CharacterSheetModel) {
        this.id = args.id;
        this.character_name = args.character_name;
        this.class = args.class;
        this.level = args.level;

    }
}

export async function createRemoteSheet() {
    const response = await post<CharacterSheetModel>(`character_sheet/create_sheet`)
    const data = response.data;
    return new CharacterSheetModel(data);
}

export async function getRemoteSheetList() {
    const response = await get<Array<CharacterSheetModel>>(`character_sheet/character_sheets`);
    return response.data.map(val => new CharacterSheetModel(val))
}

