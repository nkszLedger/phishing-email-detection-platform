//[Data Table Javascript]

//Project:	Security Analytics Admin - Responsive Admin Template
//Primary use:   Used only for the Data Table

$(document).ready(function () {
    "use strict";

    // Initialize the data table
    let table = $('#affected_accounts').DataTable();

    // Preprocess URL
	let url = window.location.href;
    url = url.split("dashboard/?")[0];
    let new_url = url+'api/affected_accounts/';

    // Fetch Data
    fetch(new_url)
    .then(response => response.json())
    .then(data => {
        // Preprocess email_from address and populate data table
        const regex = /<([^>]+)>/g;
        data.forEach(account => {
            let email_to = [
                ...account.email_to.matchAll(regex)
            ].map(m => m[1]);

            let email_from = [
                ...account.email_from.matchAll(regex)
            ].map(m => m[1]);

            table.row.add([
                account.id,
                'Oct 16, 2024',
                email_to == ""? account.email_to:email_to,
                email_from == ""? account.email_from: email_from,
                'CRITICAL', 
                'Queued'
            ]).draw()
        });
    }).catch(error => console.error("Error fetching data: ", error));
	
	
  }); // End of use strict