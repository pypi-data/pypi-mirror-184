# Gimie
# Copyright 2022 - Swiss Data Science Center (SDSC)
# A partnership between École Polytechnique Fédérale de Lausanne (EPFL) and
# Eidgenössische Technische Hochschule Zürich (ETHZ).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Tuple, Optional
from dataclasses import dataclass, field
from functools import cached_property
from pydriller import Repository
import datetime


@dataclass(order=True)
class Release:
    """
    This class represents a release of a repository.

    Parameters
    ----------
    tag: str
        The tag of the release.
    date: datetime.datetime
        The date of the release.
    commit_hash: str
        The commit hash of the release.
    """

    tag: str = field(compare=False)
    date: datetime.datetime = field(compare=True)
    commit_hash: str = field(compare=False)


class GitMetadata:
    """
    This class is responsible for extracting metadata from a git repository.

    Parameters
    ----------
    path: str
        The path to the git repository.

    Attributes
    ----------
    authors
    creation_date
    creator
    releases
    repository: Repository
        The repository we are extracting metadata from.
    """

    def __init__(self, path: str):
        self.repository = Repository(path)

    @cached_property
    def authors(self) -> Tuple[str]:
        """Get the authors of the repository."""
        return tuple(set(commit.author.name for commit in self.repository.traverse_commits()))

    @cached_property
    def creation_date(self) -> Optional[datetime.datetime]:
        """Get the creation date of the repository."""
        try:
            return next(self.repository.traverse_commits()).author_date
        except StopIteration:
            return None

    @cached_property
    def creator(self) -> Optional[str]:
        """Get the creator of the repository."""
        try:
            return next(self.repository.traverse_commits()).author.name
        except StopIteration:
            return None

    @cached_property
    def releases(self) -> Tuple[Release]:
        """Get the releases of the repository."""
        try:
            # This is necessary to initialize the repository
            next(self.repository.traverse_commits())
            releases = tuple(Release(tag=tag.name, date=tag.commit.authored_datetime,
                                     commit_hash=tag.commit.hexsha) for tag in self.repository.git.repo.tags)
            return sorted(releases)
        except StopIteration:
            return None
