import { ParplotModel, ParplotView } from './parplot';
import NimbusPref from './NimbusPref.vue';
export declare class NimbusPrefModel extends ParplotModel {
    static model_name: string;
    static view_name: string;
}
export declare class NimbusPrefView extends ParplotView {
    component: NimbusPref;
    getComponent(confs: any, maximized: any, maxAsMin: any): NimbusPref;
}
