import pytest

from robot import Robot, Direction, IllegalMoveException


@pytest.fixture
def robot():
    return Robot()


def test_constructor(robot):
    state = robot.state()

    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


def test_east_turn(robot):
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.EAST


def test_illegal_move(robot):
    robot.turn();
    robot.turn();

    with pytest.raises(IllegalMoveException):
        robot.move()

def test_full_turn(robot):
    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.EAST
    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.SOUTH
    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.WEST
    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.NORTH

def test_illegal_north(robot):
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move() #9 moves
    with pytest.raises(IllegalMoveException):
        robot.move()

def test_illegal_east(robot):
    robot.turn()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move()
    robot.move() #9 moves
    with pytest.raises(IllegalMoveException):
        robot.move()

def test_illegal_west(robot):
    robot.turn();
    robot.turn();
    robot.turn()

    with pytest.raises(IllegalMoveException):
        robot.move()



def test_move_north(robot):
    robot.move()
    state = robot.state()
    assert state['row'] == 9
    assert state['col'] == 1

def test_move_east(robot):
    robot.turn()
    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 2

def test_move_south(robot):
    robot.move()
    robot.turn()
    robot.turn()
    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 1

def test_move_west(robot):
    robot.turn()
    robot.move()
    robot.turn()
    robot.turn()
    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 1


def test_back_track_without_history(robot):
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_track_move(robot):
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 9
    assert state['col'] == 1

def test_back_track_turn(robot):
    robot.turn()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.EAST
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_track_multi_move(robot):
    robot.move()
    robot.move()
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 7
    assert state['col'] == 1

def test_back_track_all_multi_move(robot):
    robot.move()
    robot.move()
    robot.move()
    robot.back_track()
    robot.back_track()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 9
    assert state['col'] == 1

