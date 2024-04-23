__author__ = "bb"
__filename__ = "constants.py"
__description__ = "Constants required for compiler."


SYMBOL_TABLE_DUMP_FILENAME = "symtab_{}.csv"
AST_FILENAME = "ast_{}.dot"
AST_PLOT_FILENAME = "ast_plot_{}.png"
MIPSCODE_FILENAME = "{}.s"
TOKENS_TO_IGNORE = ["{", "}", "(", ")", ";", "[", "]", ","]
MAIN_FUNCTION = "main"
INBUILT_FUNCTIONS = ["printf", "scanf"]
LABELS = ["__func", ".data", ".text", ".globl", "__LABEL_", MAIN_FUNCTION]

MIPS_PRINTF = [
    ["__func_printf:"],
    ["addi", "$sp", "$sp", -4],
    ["sw", "$fp", "($sp)"],
    ["addi", "$fp", "$sp", 4],
    ["addi", "$sp", "$sp", -4],
    ["sw", "$ra", "($sp)"],
    ["li","$t8",11],
    ["bne","$t8","$v0","intfloat"],
    ["lw", "$t9", "($t7)"],
    ["addi", "$t7", "$t7", 4],
    ["printloop:"],
    ["beq","$t9", "$0","printend" ],
    ["addi", "$t9","$t9", -1],
    ["lb", "$a0", "($t7)"],
    ["syscall"],
    ["addi", "$t7", "$t7", 1],
    ["j","printloop"],
    ["intfloat:"],
    ["syscall"],
    ["printend:"],
    ["la", "$a0", "__printf_newline"],
    ["li", "$v0", 4],
    ["syscall"],
    ["lw", "$ra", -8, "($fp)"],
    ["move", "$sp", "$fp"],
    ["lw", "$fp", -4, "($fp)"],
    ["jr", "$ra"],
]

MIPS_SCANF = [
    ["__func_scanf:"],
    ["addi", "$sp", "$sp", -4],
    ["sw", "$fp", "($sp)"],
    ["addi", "$fp", "$sp", 4],
    ["addi", "$sp", "$sp", -4],
    ["sw", "$ra", "($sp)"],
    ["syscall"],
    ["lw", "$ra", -8, "($fp)"],
    ["move", "$sp", "$fp"],
    ["lw", "$fp", -4, "($fp)"],
    ["jr", "$ra"],
]