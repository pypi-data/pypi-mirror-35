import { VegaModel, VegaView } from './vega';
import Parplot from './Parplot.vue';
export declare class ParplotModel extends VegaModel {
    static model_name: string;
    static view_name: string;
}
export declare class ParplotView extends VegaView {
    component: Parplot;
    vegaElement: HTMLDivElement;
    getConfs(): any[];
    render(): void;
    getComponent(confs: any, maximized: any, maxAsMin: any): Parplot;
    addComponentWatchers(): void;
    onPrefsChange(newPrefProb: any, oldPrefProb: any): void;
    onMaxAsMinChange(newMaxAsMin: any, oldMaxAsMin: any): void;
    readonly vegaEl: HTMLDivElement;
}
