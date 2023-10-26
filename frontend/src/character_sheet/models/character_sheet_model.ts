import {post} from "../../core/api.ts";

export default class CharacterSheetModel {
    id: number
    name: string
    class: string
    level: number

    constructor(args: CharacterSheetModel) {
        this.id = args.id;
        this.name = args.name;
        this.class = args.class;
        this.level = args.level;

    }
}

export async function createRemoteSheet() {
    const response = await post<CharacterSheetModel>(`character_sheet/create_sheet`)
    const data = response.data;
    return new CharacterSheetModel(data);
}

// export async function getRemoteSheetList() {
//     const response = await getRemoteSheetList();
//     Lists.
// }
//
