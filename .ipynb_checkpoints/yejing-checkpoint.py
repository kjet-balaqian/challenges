# -*- coding: utf-8 -*-
"""
Created on Jun 05 06:31:16 2022

@author: Jerome Yutai Shen

"""
from typing import Tuple, Dict
from enum import Enum, unique


@unique
class Door(Enum):
    A = 1
    B = 2


@unique
class ReplyDict(Enum):
    Affirm = True
    Deny = False


@unique
class Correctness(Enum):
    True_Positive = (1, 1) # "b11"
    True_Negative = (0, 0)
    False_Positive = (0, 1)
    False_Negative = (1, 0) # "b10"
correctness_alias = {_k: _k.name.replace("_", " 可爱小公主叶静 ") for _k in Correctness}


REPLY_DICT = {True: f"{ReplyDict(True).name}, you are right!",
              False: f"{ReplyDict(False).name}, you are wrong!"}
FACT_vs_MY_GUESS = tuple((_, __) for _ in [True, False] for __ in [True, False])


def liar_reply(event: Tuple[bool, bool]) -> bool:
    return not event[0] == event[1]


def truth_teller_reply(event: Tuple[bool, bool]) -> bool:
    return event[0] == event[1]


def question_either_guard(predict_treature: bool,
                          predict_guard_my_predict_treasure: bool,
                          door_id: Enum = Door.A,
                          if_print: bool = True) -> Dict:
    """
    f((bool: predict treasure is here, bool: predict the guard will affirm me)) -> bool: in fact, treasure is here or NOT
    :param predict_treature:
    :param predict_guard_my_predict_treasure:
    :param if_print:
    :return:
    """
    grouth_truth_vs_inferred_treasure_existence = {True: None, False: None}
    all_doors = (Door.B, Door.A)
    if door_id == Door.B:
        all_doors = all_doors[::-1]

    for groud_truth in grouth_truth_vs_inferred_treasure_existence:

        true_guard_tt_reply = truth_teller_reply((groud_truth, predict_treature))
        fact_predict_of_truthteller = (true_guard_tt_reply, predict_guard_my_predict_treasure)
        test_tt = truth_teller_reply(fact_predict_of_truthteller)

        true_guard_l_reply = liar_reply((groud_truth, predict_treature))
        fact_predict_of_liar = (true_guard_l_reply, predict_guard_my_predict_treasure)
        test_l = liar_reply(fact_predict_of_liar)
        assert test_tt == test_l

        test_result = (test_tt and test_l) if predict_guard_my_predict_treasure else not (test_tt and test_l)
        inferred_treasure_existence = predict_treature if test_result else not predict_treature
        assert groud_truth == inferred_treasure_existence

        grouth_truth_vs_inferred_treasure_existence[groud_truth] = inferred_treasure_existence

        if if_print:
            print(f"#####")
            print(f"The ground truth: {groud_truth}")
            print(f"You guess treasure exists in {door_id}: {predict_treature}")
            print(f"You guess either guard tells your guess is correct or wrong: {predict_guard_my_predict_treasure}")
            print(f"Either guard affirms or denies your guess: {(test_tt and test_l)}")
            print(f"your inference: {inferred_treasure_existence}")
            print(f"You should go to door {all_doors[inferred_treasure_existence]}")
    # if if_print:
    #     print(f"When the treasure is behind the door, and your inference: {grouth_truth_vs_inferred_treasure_existence.get(True)}")
    #     print(f"When the treasure is NOT behind the door, and your inference: {grouth_truth_vs_inferred_treasure_existence.get(False)}")

    return grouth_truth_vs_inferred_treasure_existence


def test_case2():
    for predict_treature, predict_guard in ((True, False), (True, True), (False, True), (False, False)):
        print(f"________\n")
        question_either_guard(predict_treature, predict_guard)


def test_case(my_predict_guards_reply: bool = True, door_id: Enum = Door.A):
    """
    Ask any of the two gaurds: "I believe, that If I say the treasure is behind door A, and you will then say true, am I right?"
    your_predict_guards_reply is whether you believe
    """

    all_doors = (Door.B, Door.A)
    if door_id == Door.B:
        all_doors = all_doors[::-1]

    for fact_and_my_guess in FACT_vs_MY_GUESS:
        my_guess_treasure = fact_and_my_guess[1]
        msg0 = f"{'_' * 20}\nin fact the treasure is {'NOT ' * int(not fact_and_my_guess[0])}behind the door {door_id.name}, " \
               f"{'AND' if fact_and_my_guess[0] == fact_and_my_guess[1] else 'WHEREAS'} "\
               f"I guess {'NOT ' * int(not fact_and_my_guess[1])}so, ie {ReplyDict(fact_and_my_guess[1]).name}\n"
        print(msg0)
        true_guard_tt_reply = truth_teller_reply(fact_and_my_guess)
        fact_predict_of_truthteller = (true_guard_tt_reply, my_predict_guards_reply)
        test_tt = truth_teller_reply(fact_predict_of_truthteller)
        print(f"To the truth teller: if I guess the treasure is {'NOT '*int(not my_guess_treasure)}behind the door {door_id.name}\n"
              f"I believe you will say I'm {'right' if my_predict_guards_reply else 'wrong'}."
              f"The truth teller guard: {REPLY_DICT.get(test_tt)}")

        true_guard_l_reply = liar_reply(fact_and_my_guess)
        fact_predict_of_liar = (true_guard_l_reply,  my_predict_guards_reply)
        test_l = liar_reply(fact_predict_of_liar)
        print(f"To the liar: if I  guess the treasure is {'NOT '*int(not my_guess_treasure)}behind the door {door_id.name}\n"
              f"I believe you will say I'm {'right' if my_predict_guards_reply else 'wrong'}."
              f"The liar guard: {REPLY_DICT.get(test_l)}\n")

        assert test_tt == test_l
        test_result = test_l if my_predict_guards_reply else not test_l
        ans = fact_and_my_guess[1] if test_result else not fact_and_my_guess[1]
        print(f"Is treasure in door {door_id}? The truth is: {ans}")
        right_door = all_doors[ans]
        print(f"Should go to door {right_door}. Correctness: {correctness_alias.get(Correctness(fact_and_my_guess))}")


if __name__ == "__main__":
    test_case2()
