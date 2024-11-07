#!/usr/bin/python3

"""
Copyright (c) 2006-2024 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.convert import getOrds
from plugins.generic.syntax import Syntax as GenericSyntax

class Syntax(GenericSyntax):
    @staticmethod
    def escape(expression, quote=True):
        """
        Note: PostgreSQL has a general problem with concenation operator (||) precedence (hence the parentheses enclosing)
              e.g. SELECT 1 WHERE 'a'!='a'||'b' will trigger error ("argument of WHERE must be type boolean, not type text")

        >>> Syntax.escape("SELECT 'abcdefgh' FROM foobar") == "SELECT (CHR(97)||CHR(98)||CHR(99)||CHR(100)||CHR(101)||CHR(102)||CHR(103)||CHR(104)) FROM foobar"
        True
        """

        def escaper(value):
            return "(%s)" % "||".join("CHR(%d)" % _ for _ in getOrds(value))  # Postgres CHR() function already accepts Unicode code point of character(s)

        return Syntax._escape(expression, quote, escaper)
