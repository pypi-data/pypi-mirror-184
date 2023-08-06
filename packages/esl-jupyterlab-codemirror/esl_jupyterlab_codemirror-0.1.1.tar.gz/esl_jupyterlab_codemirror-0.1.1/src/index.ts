import {
  JupyterFrontEndPlugin,
  JupyterFrontEnd
} from '@jupyterlab/application';
import { ICodeMirror } from '@jupyterlab/codemirror';

import '../style/index.css';

const ESL_MIME_TYPE = 'text/x-esl';
const ESL_EXTENSION = '.esl';
const ESL_NAME = 'ESL';

// Token regexes
const keyword_control_define = /(?<!-)\b(define)\b(?!-)/m;
const define_class = /(?<!-)[\t ]+[\w-]+/m;
const define_nametag = /(?<!-)[\t ]+[\w-]+/m;
const continue_newline = /(\.\.\.)/m;
const asterisk = /(\*)/m;
const placeholder_value = /(?<!-)\b(t\.b\.d\.)\b(?!-)/m;
const support_function_isan = /(?<!-)\b(is[ \t]+an?)\b(?!-)/m;
const support_function_be = /(?<!-)\b(is|be)\b(?!-)/m;
const support_function_of = /(?<!-)\b(of)\b(?!-)/m;
const support_function_auxiliary_verb =
  /(?<!-)\b(shall|must|should|could|will)\b(?!-)/m;
const keyword_control_environments =
  /(?<!-)\b(world|types?|verbs?|components?|variables?|parameters?|comments?|needs?|relations?|arguments?|subclauses?|(goal|transformation|design|behavior)-(requirements?|constraints?)|variable-groups?)\b(?!-)/m;
const entity_name_tag_label = /(?<!-)\b[\w-]+:/m;
const support_function_logical =
  /(?<!-)\b((at[ \t]+most)|(at[ \t]+least)|(smaller[ \t]+than)|(greater[ \t]+than)|(equal[ \t]+to)|not|or|case|and|when|then|maximized|minimized|approximately)\b(?!-)/m;
const constant_language_types =
  /(?<!-)\b(real|string|bool|integer|enumeration)\b(?!-)/m;
const support_function_relation =
  /(?<!-)\b((relating|requiring|returning)[ \t]+(parameters?|arguments?))\b(?!-)/m;
const keyword_control_with =
  /(?<!-)\bwith[\t ]+(subclauses?|arguments?|units?)\b(?!-)/m;
const any_token = /(?<!-)\b[\w-]+\b(?!-)/m;
const property = /(?<!-)\b(property)\b(?!-)/m;
const bundle_of = /(?<!-)\b(bundle[ \t]+of)\b(?!-)/m;
const group_of = /(?<!-)\b(group[ \t]+of)\b(?!-)/m;
const empty = /(?<!-)\b(empty)\b(?!-)/m;
const support_function_fallback_case =
  /(?<!-)\b(no[ \t]+other[ \t]+case[ \t]+applies)\b(?!-)/m;
const support_function_one_or_more = /(?<!-)\b(one[ \t]+or[ \t]+more)\b(?!-)/m;

// Default state
function default_state() {
  return {
    define: 0
  };
}

// ESL mode definition
function esl_mode() {
  return {
    startState: default_state,
    token: function (stream: any, state: any) {
      // As soon as we find a comment sign, rest of the line is a comment.
      if (stream.peek() === '#') {
        stream.skipToEnd();
        return 'comment';
      }

      // Define block "define"
      if (state.define === 0) {
        if (stream.match(keyword_control_define)) {
          if (!stream.eol() || continue_newline.test(stream)) {
            state.define = 1;
          } else {
            state.define = 0;
          }
          return 'keyword';
        }
      }
      // Define block "class" (component, variable, etc.)
      else if (state.define === 1) {
        if (stream.match(define_class)) {
          if (!stream.eol() || continue_newline.test(stream)) {
            state.define = 2;
          } else {
            state.define = 0;
          }
          return 'meta';
        } else {
          state.define = 0;
        }
      }
      // Define block component nametag
      else if (state.define === 2) {
        state.define = 0;
        if (stream.match(define_nametag)) {
          return 'tag';
        }
      }

      // Simple regexes

      if (stream.match(continue_newline)) {
        return 'keyword';
      } else if (stream.match(keyword_control_environments)) {
        return 'keyword';
      } else if (stream.match(asterisk)) {
        return 'keyword';
      } else if (stream.match(support_function_relation)) {
        return 'keyword';
      } else if (stream.match(keyword_control_with)) {
        return 'keyword';
      } else if (stream.match(bundle_of)) {
        return 'keyword';
      } else if (stream.match(group_of)) {
        return 'keyword';
      } else if (stream.match(empty)) {
        return 'atom';
      } else if (stream.match(support_function_fallback_case)) {
        return 'atom';
      } else if (stream.match(constant_language_types)) {
        return 'atom';
      } else if (stream.match(placeholder_value)) {
        return 'atom';
      } else if (stream.match(support_function_isan)) {
        return 'operator';
      } else if (stream.match(support_function_be)) {
        return 'operator';
      } else if (stream.match(support_function_of)) {
        return 'operator';
      } else if (stream.match(property)) {
        return 'meta';
      } else if (stream.match(support_function_auxiliary_verb)) {
        return 'attribute';
      } else if (stream.match(support_function_logical)) {
        return 'attribute';
      } else if (stream.match(support_function_one_or_more)) {
        return 'attribute';
      } else if (stream.match(entity_name_tag_label)) {
        return 'tag';
      }
      // Match any word, but don't style it.
      else if (stream.match(any_token)) {
        state = default_state();
        return null;
      }

      // Nothing matched, reset state and eat a char for breakfast.
      state = default_state();
      stream.next();
      return null;
    }
  };
}

const extension: JupyterFrontEndPlugin<void> = {
  id: 'esl-jupyterlab-codemirror:plugin',
  autoStart: true,
  requires: [ICodeMirror],
  activate: (app: JupyterFrontEnd, cm: ICodeMirror) => {
    console.log(
      'JupyterLab extension esl-jupyterlab-codemirror is being activated...'
    );

    cm.CodeMirror.defineMode(ESL_NAME.toLowerCase(), esl_mode);
    cm.CodeMirror.defineMIME(ESL_MIME_TYPE, {
      name: ESL_NAME.toLowerCase()
    });
    cm.CodeMirror.modeInfo.push({
      ext: [ESL_EXTENSION.substring(1)],
      mime: ESL_MIME_TYPE,
      mode: ESL_NAME.toLowerCase(),
      name: ESL_NAME
    });

    console.log('Associating .esl format with newly added mode...');
    app.docRegistry.addFileType({
      name: ESL_NAME,
      displayName: 'Elephant Specification language File',
      extensions: [ESL_EXTENSION],
      mimeTypes: [ESL_MIME_TYPE],
      iconClass: 'jp-MaterialIcon jp-PasteIcon'
    });

    console.log('Done!');
  }
};

export default extension;
