import Choices from 'choices.js';
import tingle from 'tingle.js';


import initializeMoment  from './moment-apstyle';

const staffURL = 'https://datalab.dallasnews.com/staff/api/v1/staff/';

const allStaffers = [
  {
    value: '',
    label: 'Choose a staffer...',
    placeholder: true,
    active: false,
    customProperties: { firstName: '', lastName: '' },
  }
];

const moment = initializeMoment();

const roleSlugNameCrosswalk = Array.from(document.querySelectorAll('td.role-name'))
  .map(el => [el.parentElement.getAttribute('data-role'), el.textContent])
  .reduce((o, current) => { o[current[0]] = current[1]; return o; }, {});

const modal = new tingle.modal({
  footer: true,
  stickyFooter: false,
  closeMethods: ['overlay', 'button', 'escape'],
  closeLabel: "Close",
  cssClass: ['custom-class-1', 'custom-class-2'],
  onOpen: function () {
    console.log('modal open');
  },
  onClose: function () {
    console.log('modal closed');
  },
  beforeClose: function () {
    // here's goes some logic
    // e.g. save content before closing the modal
    return true; // close the modal
    return false; // nothing happens
  }
});


const openAssignmentModal = (role, rawDate) => {
  const parsedDate = moment(rawDate);

  modal.setContent(`<div class="title-area"><div class="title-elements"><h3>Create assignment</h3><h5 class="role">${
    roleSlugNameCrosswalk[role]
  }</h5><h5 class="date">${
    parsedDate.format('dddd, MMM D, YYYY')
  }</h5></div></div>` +
  '<div class="assignment-modal-form">' +
    '<select id="modal-staffer"></select>' +
    '<div class="assignment-notes form-group">' +
    '    <textarea cols="40" rows="6" class="form-control" placeholder="Notes" title="" autocomplete="nope" id="id_assignment-notes">' +
        '' +
        '</textarea>' +
    '    <label class="control-label" for="id_assignment-notes">Notes</label>' +
    '    <i class="bar"></i>' +
    '    <div class="help-block"></div>' +
    '</div>' +
  `</div>`);

  modal.open();

  const selectBox = new Choices(modal.modal.querySelector('#modal-staffer'), {
    addItems: true,
    sortFilter: (a, b) => {
      const firstNameA = a.customProperties.firstName || '';
      const firstNameB = b.customProperties.firstName || '';

      const lastNameA = a.customProperties.lastName || '';
      const lastNameB = b.customProperties.lastName || '';

      if (lastNameA.toLowerCase() !== lastNameB.toLowerCase()) {
        if (lastNameA.toLowerCase() < lastNameB.toLowerCase()) return -1;
        if (lastNameA.toLowerCase() > lastNameB.toLowerCase()) return 1;
      }

      if (firstNameA.toLowerCase() !== lastNameB.toLowerCase()) {
        if (firstNameA.toLowerCase() < lastNameB.toLowerCase()) return -1;
        if (firstNameA.toLowerCase() > lastNameB.toLowerCase()) return 1;
      }

      return 0;
    },
    // searchEnabled: true,
    // editItems: false,
    // duplicateItems: false,
    placeholderValue: 'This is a placeholder set in the config',
    searchPlaceholderValue: 'Search all staffers...',
    // searchFields: ['fullName', 'email'],
    choices: allStaffers,
    placeholder: true,
    maxItemCount: 1,
    position: 'bottom',

    callbackOnCreateTemplates: function (strToEl) {
      var classNames = this.config.classNames;
      var itemSelectText = this.config.itemSelectText;
      return {
        item: function (data) {
          console.log(data);

          const outerElClasses = [
            String(classNames.item),
            String(data.highlighted ? classNames.highlightedState : classNames.itemSelectable)
          ];

          const startingOuterTag = `<div class="${
            outerElClasses.join(' ')
          }" data-item data-id="${
            data.id
          }" data-value="${
            String(data.value)
          }" ${
            String(data.active ? 'aria-selected="true"' : '')
          } ${
            String(data.disabled ? 'aria-disabled="true"' : '')
          }>`;

          const endingOuterTag = '</div>';

          return (data.placeholder === true)
            ? strToEl([
              startingOuterTag,
              `<span class="staffer-placeholder">${
                String(data.label)
              }</span>`,
              endingOuterTag,
            ].join(' '))
            : strToEl([
              startingOuterTag,
              `<img class="staffer-mug" src="${
                (data.customProperties.imageURL === null)
                  ? String('')
                  : String(data.customProperties.imageURL)
              }" alt="${
                String(data.label)
              }" /><div class="staffer-details"><span class="staffer-name">${
                String(data.label)
              }</span><span class="staffer-email">${
                (data.customProperties.email === null)
                  ? String('(unknown email)')
                  : String(data.customProperties.email)
              }</span></div>`,
              endingOuterTag,
            ].join(' '));
        },
        choice: function (data) {
          const outerElClasses = [
            String(classNames.item),
            String(classNames.itemChoice),
            String(
              data.disabled
                ? classNames.itemDisabled
                : classNames.itemSelectable
            ),
          ];

          const startingOuterTag = `<div class="${
            outerElClasses.join(' ')
          }" data-select-text="${
            String(itemSelectText)
          }" data-choice ${
            String(
              data.disabled
                ? 'data-choice-disabled aria-disabled="true"'
                : 'data-choice-selectable'
            )
          } data-id="${
            String(data.id)
          }" data-value="${
            String(data.value)
          }" ${
            String(
              data.groupId > 0 ? 'role="treeitem"': 'role="option"'
            )
          }>`;
          const endingOuterTag = '</div>';

          return (data.placeholder === true)
            ? strToEl([
              startingOuterTag,
              `<span class="staffer-placeholder">${
                String(data.label)
              }</span>`,
              endingOuterTag,
            ].join(' '))
            : strToEl([
              startingOuterTag,
              `<img class="staffer-mug" src="${
                (data.customProperties.imageURL === null)
                  ? String('')
                  : String(data.customProperties.imageURL)
              }" alt="${
                String(data.label)
              }" /><div class="staffer-details"><span class="staffer-name">${
                String(data.label)
              }</span><span class="staffer-email">${
                (data.customProperties.email === null)
                  ? String('(unknown email)')
                  : String(data.customProperties.email)
              }</span></div>`,
              endingOuterTag,
            ].join(' '));
        },
      };
    }
  });

  // if (existingEmailValue) {
  //   selectBox.setValueByChoice(existingEmailValue);
  // }
};


const assignmentCells = document.querySelectorAll('#assignment-forms tbody tr td:not(.role-name)');

fetch(staffURL)
  .then(response => response.json())
  .then((data) => {
    console.log(data.length);
    data.forEach((staffer) => {
      if (staffer.active === true) {
        allStaffers.push({
          label: staffer.fullName,
          value: staffer.email,
          customProperties: staffer
        });
      }
    });
  })
  .catch((error) => { console.log(error); });


assignmentCells.forEach((cell, index) => {
  cell.addEventListener('click', () => {
    const roleSlug = cell.parentElement.getAttribute('data-role');
    const dateStr = cell.getAttribute('data-date');

    openAssignmentModal(roleSlug, dateStr);
  });
});
