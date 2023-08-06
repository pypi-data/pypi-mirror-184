from dateutil.parser import parse
from django.utils.translation import gettext_lazy as _
from django_countries import countries


def question_answer_validation(validationerr, question, choices=None, values=None):
    """Validate choices given to answer a specific question."""

    if not choices and not values:
        validationerr(
            _("No answer given for question: {question_title}").format(
                question_title=question.title
            ),
        )

    if question.type in ["radio", "select", "select_multiple"]:
        if values:
            raise validationerr(
                _(
                    "You can't answer a {question_type} question type with a value."
                ).format(question_type=question.type)
            )

        if not choices:
            raise validationerr(
                _(
                    "You can't answer a {question_type} question type without choices."
                ).format(question_type=question.type)
            )

        for choice in choices:
            if choice.id not in question.choices.values_list("id", flat=True):
                raise validationerr(
                    _(
                        "{choice_title} is not a valid choice for {question_title}."
                    ).format(choice_title=choice.title, question_title=question.title)
                )

    if question.type not in [
        "radio",
        "select",
        "select_multiple",
    ]:
        if choices:
            raise validationerr(
                _(
                    "You can't answer a {question_type} question type with choices."
                ).format(question_type=question.type)
            )

        if not values:
            raise validationerr(
                _(
                    "You can't answer a {question_type} question type without values."
                ).format(question_type=question.type)
            )

        if question.type == "yes_no":
            for value in values:
                if value.lower() not in ["yes", "no"]:
                    raise validationerr(
                        _(
                            "{question_type} question type accept yes or no as answer."
                        ).format(question_type=question.type)
                    )
        if question.type == "integer":
            for value in values:
                if not str(value).isnumeric():
                    raise validationerr(
                        _(
                            "{question_type} question type accept integer as answer."
                        ).format(question_type=question.type)
                    )

        if question.type == "country":
            for value in values:
                if value not in [*countries.countries.keys()]:
                    raise validationerr(
                        _(
                            "{question_type} question type accept country code as answer."
                        ).format(question_type=question.type)
                    )

        if question.type == "float":
            for value in values:
                try:
                    float(value)
                except ValueError:
                    raise validationerr(
                        _(
                            "{question_type} question type accept float as answer."
                        ).format(question_type=question.type)
                    )

        if question.type == "date":
            for value in values:
                try:
                    parse(value, fuzzy=False)
                except ValueError:
                    raise validationerr(
                        _(
                            "{question_type} question type accept date as answer."
                        ).format(question_type=question.type)
                    )
