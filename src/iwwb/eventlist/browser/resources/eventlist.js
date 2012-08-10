/*
 * Wrapper around jquery.load to allow cross domain calls
 *
 * If the browser does not support cross domain AJAX calls
 * we'll use a proxy function on the local server. For
 * performance reasons we do this only when absolutely needed.
 *
 * @param {String} url: String with an url to load (and optionally
 a selector)
 * @param {String} params: Arguments as a dictionary like object, passed to remote call
 * @param {Object} callback: A callback function that is executed when the request completes.
 *
 */
/*global document, jQuery, portal_url, pb */
(function ($) {
    "use strict";

    $.fn.loadUrl = function (url, params, callback) {

        // Split the url to the base url part and the selector
        var selector = url.split(" ")[1] || "";
        url = url.split(" ")[0];

        // if 'params' is a function
        if ($.isFunction(params)) {
            // we assume that it's the callback
            callback = params;
            params = undefined;
        }

        // we use jQuery API to detect whether a browser supports cross
        // domain AJAX calls - http://api.jquery.com/jQuery.support/
        if (!$.support.cors) {

            // change 'load' to go to our proxy view on a local server
            // and pass the orignal URL as a parameter
            params = params || {};
            params.url = url;
            url = portal_url + "/@@proxy";
        }
        this.load(url + " " + selector, params, callback);
    };

    $(document).ready(function () {

        var transform_anchor_to_text = function (sValue, iColumn) {
            /* transform anchor links to text links for exporting to formats like csv */
            if (sValue.indexOf('<a') !== -1) {
                var jsValue = $(sValue);
                return jsValue.text() + ', ' + jsValue.attr('href');
            } else {
                return sValue;
            }
        };

        $("#example").dataTable({
            oLanguage: {"sUrl": "/++resource++iwwb.eventlist/dataTables.german.txt"},
            sDom: '<"num-results"i><"pagination"p>t<"clear">lfrT', // where in DOM to inject TableTools controls
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

        $("a.training-supplier").overlay({
            onBeforeLoad: function () {

                // show the loading image
                pb.spinner.show();

                // grab the content container
                var wrap = this.getOverlay().find(".content-wrap");

                // load the page specified in the trigger and hide the loading
                // image
                wrap.loadUrl(
                    this.getTrigger().attr("href") + ' #content',
                    function () {
                        var content = $(this).children("#content"),
                            children = content.children();

                        // remove everything except h3 and div.anbieterinfos
                        $.each(children, function (index, child) {
                            var $child = $(child);
                            if (!$child.is("h3")
                                    && $child.attr("class") !== "anbieterinfos") {
                                $child.remove();
                            }
                        });

                        // hide the loading image
                        pb.spinner.hide();
                    }
                );
            }
        });

    });
}(jQuery));
