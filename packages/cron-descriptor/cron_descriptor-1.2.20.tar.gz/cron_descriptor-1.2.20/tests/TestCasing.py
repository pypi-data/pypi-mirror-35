# Copyright (C) 2016 Adam Schubert <adam.schubert@sg1-game.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tests.TestCase as TestCase
from cron_descriptor import CasingTypeEnum, DescriptionTypeEnum, ExpressionDescriptor


class TestCasing(TestCase.TestCase):

    """
    Tests casing transformation
    """

    def test_sentence_casing(self):
        self.options.casing_type = CasingTypeEnum.Sentence
        ceh = ExpressionDescriptor("* * * * *", self.options)
        self.assertEqual(
            "Every minute",
            ceh.get_description(DescriptionTypeEnum.FULL))

    def test_title_casing(self):
        self.options.casing_type = CasingTypeEnum.Title
        ceh = ExpressionDescriptor("* * * * *", self.options)
        self.assertEqual(
            "Every Minute",
            ceh.get_description(DescriptionTypeEnum.FULL))

    def test_lower_casing(self):
        self.options.casing_type = CasingTypeEnum.LowerCase
        ceh = ExpressionDescriptor("* * * * *", self.options)
        self.assertEqual(
            "every minute",
            ceh.get_description(DescriptionTypeEnum.FULL))
