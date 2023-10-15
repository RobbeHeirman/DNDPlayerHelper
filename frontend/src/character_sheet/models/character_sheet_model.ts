export default class CharacterSheetModel {
    sheetId: number;
    name: string;
    class: string;
    level: number
    constructor(sheetId:number) {
        this.sheetId = sheetId;

        this.name = "";
        this.class = "";
        this.level = 1;

    }


}

