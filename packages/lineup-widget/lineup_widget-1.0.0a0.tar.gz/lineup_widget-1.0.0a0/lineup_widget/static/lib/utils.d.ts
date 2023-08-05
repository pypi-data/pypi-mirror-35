import { LocalDataProvider, Ranking } from 'lineupjs';
export interface ILineUpRanking {
    group_by: string[];
    sort_by: string[];
    columns: string[];
}
export declare function pushRanking(data: LocalDataProvider, ranking: ILineUpRanking): Ranking;
