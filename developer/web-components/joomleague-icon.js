class JoomLeagueIcon extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
      <svg viewBox="0 0 512 512" width="1em" height="1em" aria-hidden="true">
        <path d="M256 48 402 108v118c0 107-60 188-146 238-86-50-146-131-146-238V108z" fill="currentColor"/>
        <path d="M196 152h120v33c0 41-22 73-44 88v46h43v30H197v-30h43v-46c-22-15-44-47-44-88z" fill="none" stroke="currentColor" stroke-width="18"/>
      </svg>`;
  }
}
customElements.define('joomleague-icon', JoomLeagueIcon);
