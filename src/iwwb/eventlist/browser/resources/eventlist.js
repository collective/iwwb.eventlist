$(document).ready(function () {
    var transform_anchor_to_text = function (sValue, iColumn) {
        /* transform anchor links to text links for exporting to formats like csv */
        if (sValue.indexOf('<a') !== -1) {
            var jsValue = $(sValue);
            return jsValue.text() + ', ' + jsValue.attr('href');
        } else {
            return sValue;
        }
    }

    $("#example").dataTable({
        sDom: 'T<"clear">lfrtip', // where in DOM to inject TableTools controls
        oTableTools: {
            sSwfPath: portal_url + "/++resource++jquery.datatables/extras/TableTools/media/swf/copy_cvs_xls.swf",
            aButtons: [
                {
                    sExtends: "copy",
                    fnCellRender: transform_anchor_to_text
                },
                {
                    sExtends: "csv",
                    fnCellRender: transform_anchor_to_text
                },
                {
                    sExtends: "xls",
                    fnCellRender: transform_anchor_to_text
                }
            ]
        },
        sPaginationType: "full_numbers",
        iDisplayLength: 25
    });
});
