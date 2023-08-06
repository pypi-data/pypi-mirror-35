import { Vue } from "vue-property-decorator";
import { SliderConf } from './utils';
export default class MaxAsMinPanel extends Vue {
    confs: SliderConf[];
    maximized: boolean[];
    maxAsMin: boolean;
}
