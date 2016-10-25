
from DataPalette import DataPalette

class DataPaletteInterface():
    '''
    A basic controller for interacting with one or more data palettes.
    '''

    def __init__(self, ws_url=None):
        if ws_url is None:
            raise ValueError('DataPaletteInterface error: ws_url was not defined')
        self.ws_url = ws_url


    def list_data(self, ctx, params):
        '''
        '''
        token = self._extract_token(ctx)

        if 'workspaces' not in params:
            raise ValueError('missing required field "workspaces" in parameters to list_data')
        if not isinstance(params['workspaces'], list):
            raise ValueError('"workspaces" field must be a list')

        data = []
        dp_list_filter = {}
        for w in params['workspaces']:
            dp = DataPalette(w, token=token, ws_url=self.ws_url)
            data = data + dp.list(dp_list_filter)

        data = self._remove_duplicate_data(data)

        return {
            'data': data
        }

    def add_to_palette(self, ctx, params):
        '''
        '''
        token = self._extract_token(ctx)

        if 'workspace' not in params:
            raise ValueError('missing required field "workspaces" in parameters to add_to_palette')
        if 'new_refs' not in params:
            raise ValueError('missing required field "new_refs" in parameters to add_to_palette')
        if not isinstance(params['new_refs'], list):
            raise ValueError('"new_refs" field must be a list in parameters to add_to_palette')
        for k in range(0, len(params['new_refs'])):
            ref = params['new_refs'][k]
            if 'ref' not in ref:
                raise ValueError('"new_refs" list at position ' + str(k) + ' does not contain required "ref" field')

        dp = DataPalette(params['workspace'], token=token, ws_url=self.ws_url)
        return dp.add(refs=params['new_refs'])


    def remove_from_palette(self, ctx, params):
        '''
        '''
        token = self._extract_token(ctx)

        if 'workspace' not in params:
            raise ValueError('missing required field "workspace" in parameters to remove_from_palette')
        if 'refs' not in params:
            raise ValueError('missing required field "refs" in parameters to remove_from_palette')
        if not isinstance(params['refs'], list):
            raise ValueError('"refs" field must be a list in parameters to remove_from_palette')
        for k in range(0, len(params['refs'])):
            ref = params['refs'][k]
            if 'ref' not in ref:
                raise ValueError('"refs" list at position ' + str(k) + ' does not contain required "ref" field')

        dp = DataPalette(params['workspace'], token=token, ws_url=self.ws_url)
        return dp.remove(refs=params['refs'])


    def copy_palette(self, ctx, params):
        token = self._extract_token(ctx)

        if 'from_workspace' not in params:
            raise ValueError('missing required field "from_workspace" in parameters to copy_palette')
        if 'to_workspace' not in params:
            raise ValueError('missing required field "to_workspace" in parameters to copy_palette')
        if params['from_workspace'] is params['to_workspace']:
            raise ValueError('"from_workspace" is identical to "to_workspace" in parameters to copy_palette')

        existing_palette = DataPalette(params['from_workspace'], token=token, ws_url=self.ws_url)
        new_palette = DataPalette(params['to_workspace'], token=token, ws_url=self.ws_url)

        return new_palette.create_from_existing_palette(existing_palette)

    def set_palette_for_ws(self, ctx, params):

        token = self._extract_token(ctx)

        if 'workspace' not in params:
            raise ValueError('missing required field "from_workspace" in parameters to set_palette_for_ws')
        palette_name_or_id = None
        if 'palette_name_or_id' in params:
            palette_name_or_id = params['palette_name_or_id']

        palette = DataPalette(params['workspace'], token=token, ws_url=self.ws_url)
        palette.set_palette_to_obj(new_data_palette_name_or_id=palette_name_or_id)
        return {}

    def _remove_duplicate_data(self, data):
        # Note: this is a target for optimization
        unique_refs = {}
        unique_data = []
        for d in data:
            if d['ref'] in unique_refs:
                continue
            unique_refs[d['ref']] = None
            unique_data.append(d)
        return unique_data


    def _extract_token(self, ctx):
        token = None
        if 'token' in ctx:
            token = ctx['token']
        if token is None:
            print('DataPaletteInterface warning: token was not set in context object')
        return token
