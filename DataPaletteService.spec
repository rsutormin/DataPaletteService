
#include <workspace.spec>

/*

*/
module DataPaletteService {

    /* @id ws */
    typedef string ws_ref;
    
    /* @range [0,1] */
    typedef int boolean;

    /*
        dp_ref - reference to DataPalette container pointing to given object,
        dp_refs - full list of references to DataPalette containers that
            point to given object (in contrast to dp_ref which shows only
            first item from dp_refs list).
    */
    typedef structure {
        ws_ref ref;
        Workspace.object_info info;
        ws_ref dp_ref;
        list<ws_ref> dp_refs;
    } DataInfo;

    /* String with numeric ID of workspace (working as key in mapping). */
    typedef string ws_text_id;

    /*
        data_palette_refs - mapping from workspace ID to reference to DataPalette
            container object.
    */
    typedef structure {
        list <DataInfo> data;
        mapping<ws_text_id, ws_ref> data_palette_refs;
    } DataList;


    typedef string ws_name_or_id;

    /*
        workspaces - list of workspace names or IDs (converted to strings),
        include_metadata - if 1, includes object metadata, if 0, does not. Default 0.
        TODO: pagination?
    */
    typedef structure {
        list <ws_name_or_id> workspaces;
        boolean include_metadata;
    } ListDataParams;

    funcdef list_data(ListDataParams params)
        returns (DataList data_list) authentication optional;


    /* 
        ref - is workspace reference or ref-path string
    */
    typedef structure {
        ws_ref ref;
    } ObjectReference;

    typedef structure {
        ws_name_or_id workspace;
        list <ObjectReference> new_refs;
    } AddToPaletteParams;

    typedef structure {
    } AddToPaletteResult;

    funcdef add_to_palette(AddToPaletteParams params)
        returns (AddToPaletteResult result) authentication required;


    typedef structure {
        ws_name_or_id workspace;
        list <ws_ref> refs;
    } RemoveFromPaletteParams;

    typedef structure {
    } RemoveFromPaletteResult;

    /* Note: right now you must provide the exact, absolute reference of the
    item to delete (e.g. 2524/3/1) and matched exactly to be removed.  Relative
    refs will not be matched.  Currently, this method will throw an error
    if a provided reference was not found in the palette. */
    funcdef remove_from_palette(RemoveFromPaletteParams params)
        returns (RemoveFromPaletteResult result) authentication required;


    typedef structure {
        ws_name_or_id from_workspace;
        ws_name_or_id to_workspace;
    } CopyPaletteParams;


    typedef structure {
    } CopyPaletteResult;

    funcdef copy_palette(CopyPaletteParams params)
        returns (CopyPaletteResult result) authentication required;


    typedef structure {
        ws_name_or_id workspace;
        string palette_name_or_id;
    } SetPaletteForWsParams;

    typedef structure {

    } SetPaletteForWsResult;

    /* In case the WS metadata is corrupted, or there was a manual
    setup of the data palette, this function can be used to set
    the workspace metadata to the specified palette in that workspace
    by name or ID.  If you omit the name_or_id, then the code will
    search for an existing data palette in that workspace.  Be careful
    with this one- you could thrash your palette! */
    funcdef set_palette_for_ws(SetPaletteForWsParams params)
        returns (SetPaletteForWsResult result) authentication required;
};
