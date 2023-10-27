/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CharacterSheet } from '../models/CharacterSheet';
import type { CharacterSheetPostSchema } from '../models/CharacterSheetPostSchema';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class CharacterSheetService {

    /**
     * Get Sheets
     * @returns CharacterSheet Successful Response
     * @throws ApiError
     */
    public static getSheets(): CancelablePromise<Array<CharacterSheet>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/character_sheet/character_sheets',
        });
    }

    /**
     * Create Sheet
     * Creates a new empty character sheet. Can be optionally set with starting values from the CharacterSheetPostSchema.
 * :param char_sheet: a character sheet with initial values or None.
 * :return: values of a newly created character sheet.
     * @param requestBody 
     * @returns CharacterSheet Successful Response
     * @throws ApiError
     */
    public static createSheet(
requestBody?: CharacterSheetPostSchema,
): CancelablePromise<CharacterSheet> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/character_sheet/create_sheet',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
