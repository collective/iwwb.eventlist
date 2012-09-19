/*global document, jQuery */
(function ($) {
    "use strict";

    var currCodes = [],   //list of currently selected area codes
        $txtCodes;        //textarea displaying currently selected area codes

    //If area code has already been selected, remove it from the list,
    //otherwise add it. Update textarea content at the end.
    function areaClicked(code) {
        var idx = $.inArray(code, currCodes);

        if (idx > -1) {
            currCodes.splice(idx, 1);
        } else {
            currCodes.push(code);
            currCodes = currCodes.sort();
        }

        $txtCodes.val(currCodes.join(", "));
    }

    $(document).ready(function () {
        $txtCodes = $("#txtCodes");

        //set onclick handlers for all area elements
        $("#germany_map area").each(function () {
            var code = $(this).attr("alt").split(" ")[1];

            $(this).click(function (event) {
                event.preventDefault();
                areaClicked(code);
            });
        });
    });

}(jQuery));