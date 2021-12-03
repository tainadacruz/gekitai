class NoPiecesException(Exception):
    """Lançado quando o jogador tenta botar uma peça no tabuleiro enquanto não possui nenhuma peça"""


class InvalidPositionException(Exception):
    """Tentou botar uma peça em uma posição inválida"""
