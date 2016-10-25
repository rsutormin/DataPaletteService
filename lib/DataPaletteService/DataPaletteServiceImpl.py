# -*- coding: utf-8 -*-
#BEGIN_HEADER


from DataPalette.DataPaletteInterface import DataPaletteInterface

#END_HEADER


class DataPaletteService:
    '''
    Module Name:
    DataPaletteService

    Module Description:
    
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    VERSION = "0.0.1"
    GIT_URL = "git@github.com:kbaseapps/DataPaletteService"
    GIT_COMMIT_HASH = "40396b31e1fb2a851e2ce66cc9b6c015c8e2f780"
    
    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.wsURL = config['workspace-url']
        self.data_palette_interface = DataPaletteInterface(self.wsURL)
        #END_CONSTRUCTOR
        pass
    

    def list_data(self, ctx, params):
        """
        :param params: instance of type "ListDataParams" (todo: pagination?)
           -> structure: parameter "workspaces" of list of type
           "ws_name_or_id"
        :returns: instance of type "DataList" -> structure: parameter "data"
           of list of type "DataInfo" -> structure: parameter "ref" of type
           "ws_ref" (@id ws), parameter "info" of type "object_info"
           (Information about an object, including user provided metadata.
           obj_id objid - the numerical id of the object. obj_name name - the
           name of the object. type_string type - the type of the object.
           timestamp save_date - the save date of the object. obj_ver ver -
           the version of the object. username saved_by - the user that saved
           or copied the object. ws_id wsid - the workspace containing the
           object. ws_name workspace - the workspace containing the object.
           string chsum - the md5 checksum of the object. int size - the size
           of the object in bytes. usermeta meta - arbitrary user-supplied
           metadata about the object.) -> tuple of size 11: parameter "objid"
           of type "obj_id" (The unique, permanent numerical ID of an
           object.), parameter "name" of type "obj_name" (A string used as a
           name for an object. Any string consisting of alphanumeric
           characters and the characters |._- that is not an integer is
           acceptable.), parameter "type" of type "type_string" (A type
           string. Specifies the type and its version in a single string in
           the format [module].[typename]-[major].[minor]: module - a string.
           The module name of the typespec containing the type. typename - a
           string. The name of the type as assigned by the typedef statement.
           major - an integer. The major version of the type. A change in the
           major version implies the type has changed in a non-backwards
           compatible way. minor - an integer. The minor version of the type.
           A change in the minor version implies that the type has changed in
           a way that is backwards compatible with previous type definitions.
           In many cases, the major and minor versions are optional, and if
           not provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String
        """
        # ctx is the context object
        # return variables are: data_list
        #BEGIN list_data
        data_list = self.data_palette_interface.list_data(ctx, params)
        #END list_data

        # At some point might do deeper type checking...
        if not isinstance(data_list, dict):
            raise ValueError('Method list_data return value ' +
                             'data_list is not type dict as required.')
        # return the results
        return [data_list]

    def add_to_palette(self, ctx, params):
        """
        :param params: instance of type "AddToPaletteParams" -> structure:
           parameter "workspace" of type "ws_name_or_id", parameter
           "new_refs" of list of type "ObjectReference" (todo: allow passing
           in a reference chain) -> structure: parameter "ref" of type
           "ws_ref" (@id ws)
        :returns: instance of type "AddToPaletteResult" -> structure:
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN add_to_palette
        result = self.data_palette_interface.add_to_palette(ctx, params)
        #END add_to_palette

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method add_to_palette return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def remove_from_palette(self, ctx, params):
        """
        Note: right now you must provide the exact, absolute reference of the
        item to delete (e.g. 2524/3/1) and matched exactly to be removed.  Relative
        refs will not be matched.  Currently, this method will throw an error
        if a provided reference was not found in the palette.
        :param params: instance of type "RemoveFromPaletteParams" ->
           structure: parameter "workspace" of type "ws_name_or_id",
           parameter "refs" of list of type "ws_ref" (@id ws)
        :returns: instance of type "RemoveFromPaletteResult" -> structure:
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN remove_from_palette
        result = self.data_palette_interface.remove_from_palette(ctx, params)
        #END remove_from_palette

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method remove_from_palette return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def copy_palette(self, ctx, params):
        """
        :param params: instance of type "CopyPaletteParams" -> structure:
           parameter "from_workspace" of type "ws_name_or_id", parameter
           "to_workspace" of type "ws_name_or_id"
        :returns: instance of type "CopyPaletteResult" -> structure:
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN copy_palette
        result = self.data_palette_interface.copy_palette(ctx, params)
        #END copy_palette

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method copy_palette return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION, 
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
