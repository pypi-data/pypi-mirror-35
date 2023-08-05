import { DOMWidgetModel, DOMWidgetView } from '@jupyter-widgets/base';
import { ITaggleOptions, LineUp, Taggle, LocalDataProvider } from 'lineupjs';
import './style.css';
export declare class LineUpModel extends DOMWidgetModel {
    defaults(): any;
    static serializers: {
        [x: string]: {
            deserialize?: ((value?: any, manager?: import("@jupyter-widgets/base/lib/manager-base").ManagerBase<any> | undefined) => any) | undefined;
            serialize?: ((value?: any, widget?: import("@jupyter-widgets/base/lib/widget").WidgetModel | undefined) => any) | undefined;
        };
    };
    static model_name: string;
    static model_module: string;
    static model_module_version: string;
    static view_name: string;
    static view_module: string;
    static view_module_version: string;
}
export declare class TaggleModel extends DOMWidgetModel {
    defaults(): any;
    static serializers: {
        [x: string]: {
            deserialize?: ((value?: any, manager?: import("@jupyter-widgets/base/lib/manager-base").ManagerBase<any> | undefined) => any) | undefined;
            serialize?: ((value?: any, widget?: import("@jupyter-widgets/base/lib/widget").WidgetModel | undefined) => any) | undefined;
        };
    };
    static model_name: string;
    static model_module: string;
    static model_module_version: string;
    static view_name: string;
    static view_module: string;
    static view_module_version: string;
}
export declare abstract class ALineUpView extends DOMWidgetView {
    private lineup;
    protected data: LocalDataProvider;
    render(): void;
    protected abstract createLineUp(options: Partial<ITaggleOptions>): LineUp | Taggle;
    private createData;
    private dataChanged;
    private createRankings;
    private selectionChanged;
}
export declare class LineUpView extends ALineUpView {
    protected createLineUp(options: Partial<ITaggleOptions>): LineUp;
}
export declare class TaggleView extends ALineUpView {
    protected createLineUp(options: Partial<ITaggleOptions>): Taggle;
}
