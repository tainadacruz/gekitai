from game.constants import DIRECTIONS, Color, Status
from game.exceptions import EmptyCellException, InvalidPositionException, OccupiedCellException

from game.piece import Piece
from game.player import Player


class Cell:
    def __init__(self):
        self.__piece = None

    def place_piece(self, piece: Piece) -> None:
        if self.__piece is not None:
            raise OccupiedCellException()
        self.__piece = piece

    def remove_piece(self) -> Piece:
        if self.__piece is None:
            raise EmptyCellException()
        piece = self.__piece
        self.__piece = None
        return piece

    def is_occupied(self) -> bool:
        return self.__piece is not None

    def is_empty(self) -> bool:
        return self.__piece is None

    def get_piece(self) -> Piece:
        return self.__piece


class Board:
    def __init__(self):
        self.__cells: list[list[Cell]]
        self.__players: list[Player]
        self.__status: Status
        self.__current_player: Player

        self.initialize()

    def get_status(self) -> Status:
        return self.__status

    def click(self, position: tuple[int, int]) -> None:
        if self.__status == Status.NO_MATCH:
            self.initialize()
        elif self.__status == Status.IN_PROGRESS:
            self.place_piece(position)
        elif self.__status == Status.FINISHED and (position[0] == 4 or 5) and position[1] == 8:
            self.initialize()

    def initialize(self) -> None:
        self.__cells = [[Cell() for _ in range(6)] for _ in range(6)]
        self.__players = [Player(Color.RED), Player(Color.BLUE)]
        self.__status = Status.IN_PROGRESS
        self.__current_player = self.__players[0]

        cell = self.get_cell((1, 2))
        piece = self.__players[0].place_piece()
        cell.place_piece(piece)

        cell = self.get_cell((1, 4))
        piece = self.__players[0].place_piece()
        cell.place_piece(piece)

        cell = self.get_cell((2, 3))
        piece = self.__players[0].place_piece()
        cell.place_piece(piece)

        cell = self.get_cell((4, 3))
        piece = self.__players[1].place_piece()
        cell.place_piece(piece)

        cell = self.get_cell((5, 4))
        piece = self.__players[1].place_piece()
        cell.place_piece(piece)

        cell = self.get_cell((5, 5))
        piece = self.__players[1].place_piece()
        cell.place_piece(piece)


    def get_winner(self) -> list[Player]:
        winners = []
        for player in self.__players:
            if player.has_won():
                winners.append(player)
        if len(winners) == 0:
            return False
        return winners

    def set_winner(self, player: Player) -> None:
        self.__winner = player

    def current_player(self) -> Player:
        return self.__current_player

    def flip_players(self) -> None:
        for player in self.__players:
            if player.get_color() != self.__current_player.get_color():
                self.__current_player = player
                return

    def get_player(self, color: Color) -> Player:
        for player in self.__players:
            if player.get_color() == color:
                return player

    def get_cell(self, position: tuple[int, int]) -> Cell:
        if self.position_valid(position):
            return self.__cells[position[0]][position[1]]
        raise InvalidPositionException()

    def position_valid(self, position: tuple[int, int]) -> bool:
        return 0 <= position[0] < 6 and 0 <= position[1] < 6

    def move_piece(self, source: Cell, destination: Cell) -> None:
        if destination.is_empty():
            piece = source.remove_piece()
            destination.place_piece(piece)

    def remove_piece(self, cell: Cell) -> None:
        piece = cell.remove_piece()
        owner = self.get_player(piece.get_color())
        owner.take_piece(piece)

    def check_win(self) -> bool:
        for player in self.__players:
            if not player.has_pieces():
                player.set_win()
        for x in range(6):
            for y in range(6):
                cell = self.get_cell((x, y))
                if cell.is_empty():
                    continue
                color = cell.get_piece().get_color()
                for (i, j) in [(1,1), (0,1), (1,0), (1,-1)]:
                    position = (x+i, y+j)
                    if not self.position_valid(position):
                        continue
                    cell = self.get_cell(position)
                    if cell.is_empty():
                        continue
                    if color != cell.get_piece().get_color():
                        continue
                    position = (x-i, y-j)
                    if not self.position_valid(position):
                        continue
                    cell = self.get_cell(position)
                    if cell.is_empty():
                        continue
                    if color != cell.get_piece().get_color():
                        continue
                    self.get_player(color).set_win()
        return any(p.has_won() for p in self.__players)

    def finish_match(self) -> None:
        """Alterna para o estado de vitória"""
        self.__status = Status.FINISHED

    def end_turn(self) -> None:
        if self.check_win():
            self.finish_match()
        else:
            self.flip_players()

    def place_piece(self, position: tuple[int, int]) -> None:
        if self.position_valid(position):
            cell = self.get_cell(position)
            if cell.is_occupied():
                return
        else:
            return

        player = self.current_player()
        piece = player.place_piece()
        cell.place_piece(piece)

        self.push_neighbors(position)
        self.end_turn()

    def push_neighbors(self, position: tuple[int, int]) -> None:
        for direction in DIRECTIONS:
            neighbor_position = (position[0] + direction[0], position[1] + direction[1])
            if self.position_valid(neighbor_position):
                neighbor = self.get_cell(neighbor_position)
                if neighbor.is_empty():
                    continue
            else:
                continue

            push_position = (neighbor_position[0] + direction[0], neighbor_position[1] + direction[1])
            if self.position_valid(push_position):
                push = self.get_cell(push_position)
                self.move_piece(neighbor, push)
            else:
                self.remove_piece(neighbor)
