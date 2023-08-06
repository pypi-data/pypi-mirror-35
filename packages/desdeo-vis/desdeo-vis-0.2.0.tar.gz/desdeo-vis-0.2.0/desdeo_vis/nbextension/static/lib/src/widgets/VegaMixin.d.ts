import { Vue } from "vue-property-decorator";
import * as vega from 'vega';
import { SliderConf } from './utils';
import NimbusPrefSettings from './NimbusPrefSettings.vue';
export default class VegaMixin extends Vue {
    $refs: {
        vega: Element;
        settings: NimbusPrefSettings;
    };
    confs: SliderConf[];
    vegaView: vega.View;
    vegaEl: Element;
    maximized: boolean[];
    maxAsMin: boolean;
    vegaInit(): void;
    readonly curMaxAsMin: boolean;
}
