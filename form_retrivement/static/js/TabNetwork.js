function TabNetwork(number) {
    this.number = number;

    /**
     * @return {NodeList[]}
     */
    this.getTabNetwork = function () {
        return [htmlToElements(htmlTabLinkNetwork(this.number)), htmlToElements(htmlTabContentNetwork(this.number))];
    };

// todo change tablinks to tabLinks.
    function htmlTabLinkNetwork(number) {
        return `<button onclick="openTab(event, 'network${number}','network${number.substr(0, number.indexOf('-'))}')" class="tabLinks-network${number.substr(0, number.indexOf('-'))}">network${number}</button>`;
    }

    function htmlTabContentNetwork(number) {
        return `<div id="network${number}" style="display: none;
    padding: 12px 12px;
    border: 1px solid #ccc;
    border-top: none;" class="tabContent-network${number.substr(0, number.indexOf('-'))}">
    <select>
        <option>public network</option>
        <option>privet network</option>
    </select>
    <select>
        <option>dhcp</option>
        <option>static</option>
    </select>
    <input type="text" placeholder="Enter the ip Address"  > <!--required-->
</div>`;
    }

}


