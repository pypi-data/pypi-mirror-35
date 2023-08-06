from IPython.display import display, HTML

def attribution(html_string):
    return display(HTML('''
        <script>
        $('<div id="attribution_footer" style="float:right; color:#999; background:#fff;"> </div>').css({position: 'fixed', bottom: '0px', right: 20}).appendTo(document.body);
        $('#attribution_footer').html('%s');
        </script>
        '''))

def codehider(position={'top': '110px', 'right': '20px'}):
    """
    Adds a floating code hider button to the top right of the notebook.
    """
    return display(HTML('''
        <script>
        function code_toggle() {
         var buttons = document.querySelectorAll('[id^="CodeButton_"]');
         if ($("div.input").is(':visible')){
             $("div.input").hide('500');
             for (var i = 0; i < buttons.length; i++) {
                 $(buttons[i]).val('Show code cells.');
             }
         } else {
             $("div.input").show('500');
             for (var i = 0; i < buttons.length; i++) {
                 $(buttons[i]).val('Hide code cells.');
             }
         }
        }

        $( document ).ready(function(){ $('div.input').hide() });

        if (!($('#CodeButton').length)) {
            $('<form action="javascript:code_toggle()" id="CodeButtonForm"><input type="submit" id="CodeButton_floating" value="Show code cells"></form>').css({position: 'fixed', top: "%(top)s", right: "%(right)s", background: "rgba(255, 255, 255, 0.6)"}).appendTo(document.body);
        } else {
            document.getElementById('CodeButtonForm').style.top = "%(top)s";
            document.getElementById('CodeButtonForm').style.right = "%(right)s";
            $('#CodeButton_floating').val('Show code cells');
        }

        </script>
        ''' % position))

def tableofcontent(maxlevel=3, updatefrequency=300000, exclude_ids=[], position={'top': '135px', 'right': '20px'}):
    """
    Adds a floating code hider button and table of content to the top right of
    the notebook. Only the first apperance of equal headlines is linked. This
    can also be used to add a table of content somewhere in a markdown cell.

    To add a table of content in a markdown cell use the following code:
        <h2 id="tocheading">Table of Content</h2>
        <div id="tocinline"></div>

    maxlevel: Set the max level to which headlines are added.
    """
    position.update({'maxlevel': maxlevel})
    position.update({'updatefrequency': updatefrequency})
    position.update({'exclude': '['+','.join(['"'+e+'"' for e in exclude_ids])+']'})
    return display(HTML('''<script>
// Converts integer to roman numeral
function romanize(num) {
    var lookup = {M:1000,CM:900,D:500,CD:400,C:100,XC:90,L:50,XL:40,X:10,IX:9,V:5,IV:4,I:1},
        roman = '',
        i;
    for ( i in lookup ) {
        while ( num >= lookup[i] ) {
        roman += i;
        num -= lookup[i];
        }
    }
    return roman;
}

// Builds a <ul> Table of Contents from all <headers> in DOM
function createTOC(toc_tag, maxlevel){
    var toc = "";
    var level = 0;
    var levels = {};
    $('#'+toc_tag).html('');

    $(":header").each(function(i){
        if (this.id=='tocheading'){return;}
        if (this.tagName[1] >= maxlevel){return;}

        var titleText = this.innerHTML;
        var openLevel = this.tagName[1];

        var exclude = %(exclude)s;
        for (var i = 0; i < exclude.length; i++) {
            if (titleText.indexOf(exclude[i]) !== -1){return;}
        }

        if (levels[openLevel]){
        levels[openLevel] += 1;
        } else{
        levels[openLevel] = 1;
        }

        if (openLevel > level) {
        toc += (new Array(openLevel - level + 1)).join('<ul class="'+toc_tag+'">');
        } else if (openLevel < level) {
        toc += (new Array(level - openLevel + 1)).join("</ul>");
        for (i=level;i>openLevel;i--){levels[i]=0;}
        }

        level = parseInt(openLevel);

        if (this.id==''){this.id = this.innerHTML.replace(/ /g,"-")}
        var anchor = this.id;

        toc += '<li><a href="#' + escape(anchor) + '">'
        + romanize(levels[openLevel].toString()) + '. ' + titleText
        + '</a></li>';

    });

    if (level) {
    toc += (new Array(level + 1)).join("</ul>");
    }

    $('#'+toc_tag).append(toc);
};

$('<div id="toc"></div>').css({position: 'fixed', top: '160px', right: 20, background: "rgba(255, 255, 255, 0.6)"}).appendTo(document.body);
$("#toc").css("z-index", "2000");

// Executes the createToc function
setTimeout(function(){createTOC('toc', 1 + %(maxlevel)s);},100);
setTimeout(function(){createTOC('toc', 1 + %(maxlevel)s);},5000);
setTimeout(function(){createTOC('toc', 1 + %(maxlevel)s);},15000);

// Rebuild TOC every 5 minutes
setInterval(function(){createTOC('toc', 1 + %(maxlevel)s);}, %(updatefrequency)s);

function toc_toggle() {
 if ($('#toc').is(':visible')){
     $('#toc').hide('500');
     $('#tocButton').val('Show table of content')
 } else {
     $('#toc').show('500');
     $('#tocButton').val('Hide table of content')
 }
}

if (!($('#tocButton').length)) {
    $('<form action="javascript:toc_toggle()" id="tocButtonForm"><input type="submit" id="tocButton" value="Hide table of content"></form>').css({position: 'fixed', top: "%(top)s", right: "%(right)s", background: "rgba(255, 255, 255, 0.6)"}).appendTo(document.body);
} else {
    document.getElementById('tocButtonForm').style.top = "%(top)s";
    document.getElementById('tocButtonForm').style.right = "%(right)s";
    $('#tocButton').val('Hide table of content')
}

</script>
''' % position))
