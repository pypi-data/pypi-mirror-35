import Vue, { VueConstructor } from 'vue';
import VegaMixin from './VegaMixin';
declare const Parplot_base: (new (...args: any[]) => VegaMixin & Vue) & VueConstructor<Vue>;
export default class Parplot extends Parplot_base {
    mounted(): void;
}
