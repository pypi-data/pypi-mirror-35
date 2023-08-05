import { IJupyterWidgetRegistry } from '@jupyter-widgets/base';
/**
 * The lineUp plugin.
 */
declare const lineupPlugin: {
    id: string;
    requires: import("@phosphor/coreutils/lib/token").Token<IJupyterWidgetRegistry>[];
    activate: typeof activateWidgetExtension;
    autoStart: boolean;
};
export default lineupPlugin;
/**
 * Activate the widget extension.
 */
declare function activateWidgetExtension(_app: any, registry: IJupyterWidgetRegistry): void;
