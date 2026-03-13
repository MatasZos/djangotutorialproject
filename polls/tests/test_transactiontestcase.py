from django.test import TransactionTestCase
from django.utils import timezone

from polls.models import Question


class QuestionTransactionTests(TransactionTestCase):
    def test_create_question_in_database(self):
        Question.objects.create(
            question_text="Transaction test question?",
            pub_date=timezone.now(),
        )
        self.assertEqual(Question.objects.count(), 1)