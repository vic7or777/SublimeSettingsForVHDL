import sublime
import sublime_plugin
from.import vhdl_interface as face

class PasteAsProcess(sublime_plugin.TextCommand):
    def run(self, edit):
        # global _interface
        # snippet_ce = "Packages/VHDL Mode/Snippets/proc_ce.sublime-snippet"
        # snippet_clk = "Packages/VHDL Mode/Snippets/proc_clk.sublime-snippet"
        # snippet_rst = "Packages/VHDL Mode/Snippets/proc_rst.sublime-snippet"
        # self.view.run_command("vhdl_mode_insert_header")
        # ${ENAME}

        snippet_clk = "Packages/VHDL Mode/Snippets/test.sublime-snippet"
        in_port_str = face._interface.in_port()
        out_port_str = face._interface.out_port()

        self.view.run_command("insert_snippet",
            {
              "name"     : snippet_clk,
              "DATAINPORTS" : in_port_str,
              "OUTPORTS" : out_port_str
            })

        print('paste_as_process')
