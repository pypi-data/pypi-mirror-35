// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

import {
  JupyterLab, JupyterLabPlugin
} from '@jupyterlab/application';

import {
  IJupyterWidgetRegistry
 } from '@jupyter-widgets/base';

import {
  SidePanelModel
} from './SidePanelModel';

import {
  SidePanel
} from './SidePanel';

import {
  EXTENSION_SPEC_VERSION
} from './version';

const EXTENSION_ID = '@regulus/sidepanel';

const sidepanelPlugin: JupyterLabPlugin<void> = {
  id: EXTENSION_ID,
  requires: [IJupyterWidgetRegistry],
  activate: activateSidepanelExtension,
  autoStart: true
};

export default  sidepanelPlugin;

/**
 * Activate the extension.
 */
function activateSidepanelExtension(app: JupyterLab, registry: IJupyterWidgetRegistry): void {
  let AppSidePanel = class extends SidePanel {
    constructor(options: any) {
      super({app, ...options});
    }
  }

  registry.registerWidget({
    name: EXTENSION_ID,
    version: EXTENSION_SPEC_VERSION,
    exports: {
      SidePanelModel: SidePanelModel,
      SidePanel: AppSidePanel
    }
  });
}
