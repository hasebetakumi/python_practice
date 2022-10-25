
import unittest
from unittest.mock import MagicMock
from unittest import mock

import salary178


class TestSalary(unittest.TestCase):
    def test_calculation_salary(self):
        s = salary178.Salary(year=2017)
        # 疑似的に「１」を返す
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 101)

        # 179. mock.assert
        # ちゃんとbonus_priceが呼ばれたのか
        s.bonus_api.bonus_price.assert_called()

        # ループとかで複数回呼び出されず、一回だけ呼ばれたか
        s.bonus_api.bonus_price.assert_called_once()

        # 引数をしっかり渡せているか
        s.bonus_api.bonus_price.assert_called_once_with(year=2017)

        # 一度だけ呼ばれて、引数ちゃんと渡しているか
        s.bonus_api.bonus_price.assert_called_once_with(year=2017)

        # 何回bonus_priceが呼ばれたか
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1)

    def test_calculation_salary_no_bonus(self):
        s = salary178.Salary(year=2022)
        # 疑似的に「１」を返す
        s.bonus_api.bonus_price = MagicMock(return_value=0)
        self.assertEqual(s.calculation_salary(), 100)
        # 直接０を渡したのでbonus_priceは呼び出していない→エラー
        # s.bonus_api.bonus_price.assert_called()
        # not_calledにしてあげれば通る
        s.bonus_api.bonus_price.assert_not_called()

    # 180. mock.patch→メソッドを呼ぶ前にmockを宣言→mockのし忘れがない→安全
    @mock.patch('salary178.ThirdPartyBonusRestApi.bonus_price', return_value=1)
    def test_calculation_salary_patch(self, mock_bonus):
        s = salary178.Salary(year=2017)
        # 実はこれは良くない→上の行でオブジェクトを作ってからmagicmockを読んでいる
        # →mockを使わずbonus_priceを呼んでしまう可能性がある。
        # s.bonus_api.bonus_price = MagicMock(return_value=0)
        self.assertEqual(s.calculation_salary(), 101)
        # 以下のように書き換える
        mock_bonus.assert_called()

    # withを使ってもかける→mockを使わない処理を同じメソッド内に同居できる
    def test_calculation_salary_patch_with(self):
        with mock.patch('salary178.ThirdPartyBonusRestApi.bonus_price') as mock_bonus:
            mock_bonus.return_value = 1
            
            s = salary178.Salary(year=2017)
            self.assertEqual(s.calculation_salary(), 101)
            mock_bonus.assert_called()

    # patcherも使える
    def test_calculation_salary_patch_pather(self):
        # setupでスタート、teardownでstopすると便利
        patcher = mock.patch('salary178.ThirdPartyBonusRestApi.bonus_price')
        mock_bonus = patcher.start()  
        mock_bonus.return_value = 1
        
        s = salary178.Salary(year=2017)
        self.assertEqual(s.calculation_salary(), 101)
        mock_bonus.assert_called()
        
        patcher.stop()
    
    # 181. mock.side_effect→return_valueを関数を用いて定義したい
    # 例外処理もこれを用いる
    def test_calculation_salary_patch_side_effect(self):
        # setupでスタート、teardownでstopすると便利
        patcher = mock.patch('salary178.ThirdPartyBonusRestApi.bonus_price')
        mock_bonus = patcher.start() 

        # 疑似的に渡す値を関数で指定できる
        def f(year):
            return 1
        mock_bonus.side_effect = f
        # 簡単な関数ならラムダで返してもいい
        # mock_bonus.side_effect = lambda year: 1

        s = salary178.Salary(year=2017)
        self.assertEqual(s.calculation_salary(), 101)
        mock_bonus.assert_called()
        
        patcher.stop()


if __name__ == '__main__':
    test = TestSalary()
    test.test_calculation_salary()
    test.test_calculation_salary_no_bonus()
    test.test_calculation_salary_patch()
    test.test_calculation_salary_patch_with()
    test.test_calculation_salary_patch_pather()
    test.test_calculation_salary_patch_side_effect()

