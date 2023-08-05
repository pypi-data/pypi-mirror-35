import $ from 'jquery';
import {
  ripple,
  select
} from 'immaterial-ui';

console.log('ASDF 9989');

$(document).ready(() => {
  window.selectBoxes = $('select.select').map(select.build);
});
