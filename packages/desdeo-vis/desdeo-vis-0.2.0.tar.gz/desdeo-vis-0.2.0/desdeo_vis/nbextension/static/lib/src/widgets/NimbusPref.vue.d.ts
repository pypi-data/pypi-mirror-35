import Vue, { VueConstructor } from 'vue';
import { DimPref } from './utils';
import SliderOverlay from './SliderOverlay.vue';
import NimbusPrefSettings from './NimbusPrefSettings.vue';
import VegaMixin from './VegaMixin';
declare const NimbusPref_base: (new (...args: any[]) => VegaMixin & Vue) & VueConstructor<Vue>;
export default class NimbusPref extends NimbusPref_base {
    $refs: {
        vega: Element;
        settings: NimbusPrefSettings;
        sliders: SliderOverlay[];
    };
    initPreferences: DimPref[] | null;
    preferences: {
        pref: DimPref;
    }[];
    initialPreferences(): {
        pref: DimPref;
    }[];
    mounted(): void;
    readonly problem: string | null;
    readonly prefs: DimPref[];
}
